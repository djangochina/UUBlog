/**
 *  jquery.msgbox 7.1 - 2011-06-28
 *
 *  Author: pwwang
 *  Website: http://pwwang.com
 *  Note: All the stuff written by pwwang
 *	   Feel free to do whatever you want with this file
 *	   Please keep the distribution information.
 *
 **/

(function($) {

	$.msgbox = function(opts) {

		// if a string directly given, make it a text type msgbox
		if (typeof(opts) == 'string') {
			var content = opts;
			opts = {content: content};
		}

		// extend opts, set default options
		opts = opts || {};
		// msgbox width, default 360px; $('body').width is set if width is greater than that.
		opts.width = (opts.width || 360) > $('body').width() ? $('body').width() : (opts.width || 360);
		// msgbox height, default 260px; $('body').height is set if height is greater than that.
		opts.height = (opts.height || 180) > $('body').height() ? $('body').height() : (opts.height || 180);
		// title
		opts.title = opts.title || 'Information';
		// content, should be url if type is either url or ajax
		opts.content = opts.content || 'Thanks for using jquery.msgbox';
		// background opacity, default 0.6
		opts.bgOpacity = opts.bgOpacity || 0.6;
		// cache, if set to false, remove the dom after close it, else just hide it
		opts.cache = typeof opts.cache == 'undefined' ? false : opts.cache;
		// plugins on and off
		opts.pluginsOn = opts.pluginsOn || [];
		opts.pluginsOff = opts.pluginsOff || [];

		this.opts = opts;
		this._hook_options();

		this.background = $('<div />').css({
			'position': 'fixed',
			'width': $(window).width() + 'px',
			'height': $(window).height() + 'px',
			'z-index': 99,
			'opacity': this.opts.bgOpacity,
			'top': 0,
			'left': 0,
			'display': 'none'
		}).appendTo('body').addClass('jMsgbox-background');

		this.mainWrap = $('<div />').css({
			'width': this.opts.width + 'px',
			'position': 'fixed',
			'z-index': 100,
			'display': 'none',
			'left': ($(window).width() - this.opts.width) / 2 + 'px',
			'top' : ($(window).height() - this.opts.height) / 2 + 'px'
		}).appendTo('body').addClass('jMsgbox-mainWrap');

		this.headWrap = $('<div />').appendTo(this.mainWrap).addClass('jMsgbox-headWrap');

		this.titleWrap = $('<div />').css({
			'float': 'left',
			'width': (this.opts.width - 50) + 'px'
		}).html(this.opts.title).appendTo(this.headWrap).addClass('jMsgbox-titleWrap');

		var _this = this;
		this.closeWrap = $('<div />').css({  // it is a, not div
			'text-align': 'right'
		}).append('<a href="javascript:;">×</a>').appendTo(this.headWrap).find('a').click(function() {
			_this.close();
		}).addClass('jMsgbox-closeWrap');
		
		// this div is to prevent padding to break the msgbox
		// append to this is for plugins to operate
		this.contentWrapWrap = $('<div />').css({ 
			'display': 'block',
			'width': this.opts.width + 'px',
			'height': (this.opts.height - 24) + 'px',
			'overflow': 'auto' 
		}).appendTo(this.mainWrap);
		
		this.contentWrap = $('<div />').appendTo(this.contentWrapWrap).html(this.opts.content).addClass('jMsgbox-contentWrap');
		
		this._hook_domready();
		
		return this;  // to allow chain operation
	}

	$.msgbox.prototype = {

		/*****************************************
		 *  member functions
		 *  functions with prefix _ are supposed
		 *  to be private functions
		 *****************************************/

		show: function() {
			this.background.show();
			this.mainWrap.show();
			return this;
		},

		close: function() {
			if( this.opts.cache ){
				this.background.hide();
				this.mainWrap.hide();
			} else {
				this.remove();
			}
			return this;
		},
		
		remove: function(){ // anyway remove it
			this.background.remove();
			this.mainWrap.remove();
			return this;
		},

		/*****************************************
		 *  hooks for plugins
		 *  To apply plugin actions to msgbox
		 *****************************************/

		// to handle extra options for plugins
		_hook_options: function() {
			for (var pluginName in $.msgbox)
				if (this.is_active(pluginName) && $.msgbox[pluginName].options)
					$.msgbox[pluginName].options.apply(this, arguments);
		},

		// after dom setup
		_hook_domready: function() {
			for (var pluginName in $.msgbox)
				if (this.is_active(pluginName) && $.msgbox[pluginName].domready)
					$.msgbox[pluginName].domready.apply(this, arguments);
		},
		
		/*****************************************
		 *  helpers for plugins
		 *****************************************/
		
		// helper for rewrite the existed member functions, or add opts
		extend: function(name, v){
			if( $.isFunction(this[name]) && !/^_|^extend$|^is_active$/.test(name) ){
				// inline functions and '_' prefixed functions  are not allowed to be extended
				var self = this[name];
				this[name] = function(){
					v.call(this, self);
					return this;
				}
			} else {
				if( typeof this.opts[name] == 'undefined' )
					this.opts[name] = v;
			}
			return this;
		},
		
		// if a plugin is activated, for plugin development
		is_active: function(pluginName){
			return !$.msgbox[pluginName] || $.inArray(pluginName, this.opts.pluginsOn) > -1 ||
				( $.inArray(pluginName, this.opts.pluginsOff) < 0 &&
				  ( typeof $.msgbox[pluginName].active == 'undefined' || $.msgbox[pluginName].active )
				);
		}

	};
	
	//////////////////////////////////////////////////
	//                                              //
	//    jquery.msgbox internal plugins start.     //
	//    You can put your plugins somewhere else,  //
	//    as well as these plugins ... ;)           //
	//                                              //
	//////////////////////////////////////////////////
	
	/**
	 * description: enable|disable drag and drop for msgbox
	 * options added: allowDrag(true|false)
	 * ! you need to refer jquery.dragndrop plugin
	 **/
	$.msgbox.dragndrop = {

		options: function() {
			this.extend('allowDrag', true);
		},

		domready: function() {
			var _this = this;
			if (this.opts.allowDrag) {
				this.mainWrap.Drags({
					handler: this.titleWrap,
					range: 'window',
					onDrop: function() {
						// for resetposition plugin to keep the relative postion of msgbox
						_this.mainWrap.css('position', 'fixed');
						_this.relTop = _this.mainWrap.offset().top - $(window).scrollTop();
						_this.relLeft = _this.mainWrap.offset().left - $(window).scrollLeft();
					}
				});
			}
		}
	};
	
	/**
	 * description: reset the msgobx position while window is resizing or scrolling
	 **/
	$.msgbox.resetposition = {
		
		domready: function(){
			var _this = this;
			
			var resetPos = function(){
				_this.background.css({
					width: $(window).width() + 'px',
					height: $(window).height() + 'px',
					top: 0,
					left: 0
				});
				
				if( _this.relTop ){  // have been dragged
					_this.mainWrap.css({
						top: _this.relTop + 'px',
						left: _this.relLeft + 'px' 
					});
				} 
			}
			
			resetPos();
			
			$(window)
                .load(resetPos)    // just in case user is changing size of page while loading
                .resize(resetPos)
                .scroll(resetPos);
		}
		
	}
	
	
	/**
	 * description: allow to set a a user-defined close icon
	 * options added: closeIcon(string)
	 *	if it is a naked string, a 'text:' prefix will be added
	 *	closeIcon with 'text:' prefix will be directly display in closeWrap
	 *  closeIcon with 'image:' prefix will be display an image with closeIcon as its src in closeWrap
	 **/
	$.msgbox.closeicon = {

		options: function(){
			this.extend('closeIcon', '×');
			if( !/^text:|^image:/.test(this.opts.closeIcon) )
				this.opts.closeIcon = 'text:' + this.opts.closeIcon;
		},
		
		domready: function(){
			if( /^text:/.test(this.opts.closeIcon) ){
				this.closeWrap.html(this.opts.closeIcon.substr(5));
			} else {
				this.closeWrap.html('<img src="'+ this.opts.closeIcon.substr(6) +'" />');
			}
		}
		
	}
	
	/**
	 * description: add a callback when msgbox is closing
	 * options added: onClose(function)
	 * function modified: close
	 **/
	$.msgbox.onclose = {
		
		options: function(){
			this.extend('onClose', function(){});
		},
		
		domready: function(){
			this.extend('close', function(self){
				self.call(this);
				this.opts.onClose.apply(this, arguments);
			});
		}
	};
	
	/**
	 * description: add a function that msgbox will be automatically closed in autoclose seconds
	 * options added: autoclose(int), 0 to disable this function
	 * functions added:
	 * 	startAutoClose(int): manually start auto-closing
	 *		if autoclose is set to 0, you can use this function to start auto-closing
	 *	endAutoClose: to end auto-closing immediately
	 * functions modified:
	 *	close: to prevent timer running after close
	 **/
	$.msgbox.autoclose = {
		
		options: function() {
			this.extend('autoClose', 0);
		},
		
		domready: function(){
			
			var _this = this;
			this.closeMsg = '&nbsp; &nbsp; Closing in <strong>{seconds}</strong>s';
			var interval = null;
			var autoclose = function(sec){
				_this.titleWrap.append(_this.closeMsg.replace('{seconds}', sec));
				
				interval = setInterval(function(){
					if( sec==1 ){
						_this.close();
					} else {
						sec--;
						$('strong', _this.titleWrap).text(sec);
					}
				}, 1000);
			};
				
			// to prevent timer running after msgbox closed
			this.extend('close', function(self){
				self.call(this);
				clearInterval(interval);
			});
				
			this.startAutoClose = function(sec){
				if( sec > 0 )
					autoclose.call(_this, sec);
				return _this;
			};
			
			this.endAutoClose = function(){
				_this.titleWrap.html( this.opts.title );
				clearInterval(interval);
				return _this;
			};
			
			this.startAutoClose(this.opts.autoClose);
		}
	}
	
	/**
	 * description: add animation when opening and closing
	 * options added: anim(int) type of animation to add, default: 0
	 * functions modified:
	 * 	show
	 * 	close
	 **/
	$.msgbox.animate = {

		options: function(){
			this.extend('anim', 0);
		},
		
		domready: function(){
			var _this = this;
			this.extend('show', function(self){
				this.background.show();
				switch(this.opts.anim){
					case 0:
						_this.mainWrap.show().css({
							top: (_this.mainWrap.offset().top - 40) + 'px',
							opacity: .3
						}).animate({
							top: (_this.mainWrap.offset().top + 40) + 'px',
							opacity: 1
						}, function(){
							// loading start, avoid choking when loading content and animation happen at the same time
							_this.startLoading = true; 
							self.call(_this);
						});
						break;
					case 1:
						_this.mainWrap.show().css({
							left: (_this.mainWrap.offset().left - 80) + 'px',
							opacity: .3
						}).animate({
							left: (_this.mainWrap.offset().left + 80) + 'px',
							opacity: 1
						}, function(){
							// loading start, avoid choking when loading content and animation happen at the same time
							_this.startLoading = true; 
							self.call(_this);
						});
						break;
					case 2:
						_this.mainWrap.show().css({
							left: (_this.mainWrap.offset().left + 80) + 'px',
							opacity: .3
						}).animate({
							left: (_this.mainWrap.offset().left - 80) + 'px',
							opacity: 1
						}, function(){
							// loading start, avoid choking when loading content and animation happen at the same time
							_this.startLoading = true; 
							self.call(_this);
						});
						break;
					default:
						self.call(_this);
						break;
				}
			});
			
			this.extend('close', function(self){
				switch(this.opts.anim){
					case 0:
						this.mainWrap.animate({
							top: (this.mainWrap.offset().top - 40) + 'px',
							opacity: 0
						}, function(){
							self.call(_this);
						});
						break;
					case 1:
						this.mainWrap.animate({
							left: (this.mainWrap.offset().left - 80) + 'px',
							opacity: 0
						}, function(){
							self.call(_this);
						});
						break;
					case 2:
						this.mainWrap.animate({
							left: (this.mainWrap.offset().left + 80) + 'px',
							opacity: 0
						}, function(){
							self.call(_this);
						});
						break;
					default:
						self.call(_this);
						break;
				}
			});
		}
	}
	
	/**
	  * description: fix the dimension
	  **/
	$.msgbox.fixdimen = {
		domready: function(){
			this.extend('show', function(self){
				// need to show first, because some of the dimensions cannot be got if they are hidden.
				self.apply(this, arguments);
				// fix titleWrap width
				var _this = this;
				var interval = setInterval(function(){ // wait until the image loaded
					if( _this.closeWrap.outerWidth(true) > 0 ){
						clearInterval(interval);
						_this.titleWrap.width( _this.opts.width - 
											  _this.closeWrap.outerWidth(true) - 
											  parseInt(_this.headWrap.css('padding-left')) -
											  parseInt(_this.headWrap.css('padding-right')) -
											  parseInt(_this.headWrap.css('border-right-width')) -
											  parseInt(_this.headWrap.css('border-left-width')) -
											  parseInt(_this.headWrap.css('margin-left')) -
											  parseInt(_this.headWrap.css('margin-right')) - 5 );
					}
				}, 200);
				
				// fix contentWrapWrap height
				this.contentWrapWrap.height(this.opts.height - this.headWrap.outerHeight(true));
			});
		}
	};
		
	/**
	 * description: add multiple type support for msgbox
	 * options added:
	 * 	type(string)
	 * 		alert: add a close button at the bottom
	 * 		confirm: add YES,NO button at the bottom
	 * 		input: add a input box and a OK button
	 * 		ajax/url: opts.content should be a url for ajax
	 * 		iframe: opts.content should be a url for iframe
	 * 		anything else: a plain text(HTML supported) string in content wrapper
	 * 	onAjaxed(function)
	 * 		callback when ajax request completed.
	 **/
	$.msgbox.contenttype = {
		
		options : function(){
			this.extend('type', 'text');
			this.extend('onAjaxed', function(){});
		},
		
		domready: function(){
			var _this = this;
			switch(this.opts.type){
				case 'alert':
					
					var closebutton = $('<input type="button" value=" OK " />').click(function(){
						_this.close();	
					});
					var center = $('<center />').css('padding','8px').append(closebutton);
					this.mainWrap.append(center);
					
					// fix contentWrapWrap height
					_this.extend('show', function(self){
						self.apply(this, arguments);
						_this.contentWrapWrap.height(this.opts.height - this.headWrap.outerHeight(true) - center.outerHeight(true));
					});
					
					break;
				case 'confirm':
					_this.contentWrapWrap.height(parseInt(_this.contentWrapWrap.css('height'))-40);
					this.setValue = function(v){
						_this.value = v;
						return _this;
					};
					this.getValue = function(){
						return _this.value;
					}
					var yesbutton = $('<input type="button" value=" Yes " />').click(function(){
						_this.setValue( true );
						_this.close();	
					});
					var nobutton = $('<input type="button" value=" No " />').click(function(){
						_this.setValue( false );
						_this.close();	
					});
					var center = $('<center />').css('padding','8px').append(yesbutton).append('&nbsp;').append(nobutton);
					this.mainWrap.append(center);
					
					// fix contentWrapWrap height
					_this.extend('show', function(self){
						self.apply(this, arguments);
						_this.contentWrapWrap.height(this.opts.height - this.headWrap.outerHeight(true) - center.outerHeight(true));
					});
					break;
				case 'input':
					_this.contentWrapWrap.height(parseInt(_this.contentWrapWrap.css('height'))-40);
					this.setValue = function(v){
						_this.value = v;
						return _this;
					};
					this.getValue = function(){
						return _this.value;
					}
					var inputbox = $('<input type="text" />');
					var okbutton = $('<input type="button" value=" OK " />').click(function(){
						_this.setValue( inputbox.val() );
						_this.close();
					});
					var div = $('<div />').css('padding','8px').append(inputbox).append('&nbsp;').append(okbutton);
					this.mainWrap.append(div);
					
					// fix contentWrapWrap height
					_this.extend('show', function(self){
						self.apply(this, arguments);
						_this.contentWrapWrap.height(this.opts.height - this.headWrap.outerHeight(true) - div.outerHeight(true));
					});
					break;
				case 'ajax':
				case 'url':
					_this.contentWrap.text('Loading ...');
					if( !_this.is_active('animate') )
						_this.startLoading = true;
					var interval = setInterval(function(){ // avoid choking while animating
						if( _this.startLoading ){
							clearInterval(interval);
							_this.contentWrap.load(_this.opts.content, function(){
								_this.opts.onAjaxed.apply(_this, arguments);
							});
						}
					}, 200);
					break;
				case 'iframe':
					this.contentWrap.css('padding',0).empty();
					if( !_this.is_active('animate') )
						_this.startLoading = true;
					var interval = setInterval(function(){
						if( _this.startLoading ){ 
							clearInterval(interval);
							$('<iframe border="0" frameborder="0" marginheight="0" marginwidth="0" scrolling="auto"></iframe>')
								.appendTo(_this.contentWrap)
								.css({
									'height': '100%',
									'width': '100%'
								})
								.attr({
									'width'  : '100%',
									'height' : '100%',
									'src'    : _this.opts.content
								});
						}
					}, 200);
					break;
				default:
					break;
				
			}
		}
	}
	
	/**
	 * description: flash the title when clicking the background
	 **/
	$.msgbox.flashtitle = {
		domready: function(){
			var _this = this;
			var timeout = null;
			var flash = function(opacity, times, interval, flag){
				if( times > 0 ) {
					flag = !flag;
					op = flag ? opacity : 1;
					this.headWrap.css('opacity',op);    
					timeout = setTimeout(function(){ flash.call(_this, opacity, times-1, interval, flag) }, interval);
				} else clearTimeout(timeout);
			}
			
			this.background.click(function(){
				flash.call(_this, .5, 4, 80);
			});
		}
	}
		
	/**
	 * description: allow double-click background to close msgbox
	 **/
	$.msgbox.bgdblclick2close = {
		domready: function(){
			var _this = this;
			this.background.dblclick(function(){
				_this.close();	
			})
		}
	}
	
	/**
	 * description: allow option showClose to control if msgbox could be closed.
	 *				but it can still be closed by function(this.close)
	 * options added: showClose(true|false)
	 * functions added:
	 * 	setShowClose(true|false):
	 * 		show or hide close icon, if background dblclick close set, enable or disabled it
	 **/
	$.msgbox.showclose = {
		
		options: function(){
			this.extend('showClose', true);
		},
		
		domready: function(){
		
			var _this = this;
			this.setShowClose = function(sc){
				if( sc ){
					_this.closeWrap.css('visibility', 'visible');
					if( _this.is_active('bgdblclick2close') ) {
						_this.background.unbind('dblclick'); // in case it has already bound.
						_this.background.dblclick(function(){
							_this.close();
						});
					} 
				} else {
					_this.closeWrap.css('visibility', 'hidden');
					_this.background.unbind('dblclick');
				}
				return _this;
			}
			this.setShowClose(this.opts.showClose);
		}
		
	}

})(jQuery);
