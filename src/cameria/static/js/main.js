// Hive Cameria System
// Copyright (C) 2008-2014 Hive Solutions Lda.
//
// This file is part of Hive Cameria System.
//
// Hive Cameria System is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Hive Cameria System is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Hive Cameria System. If not, see <http://www.gnu.org/licenses/>.

// __author__    = João Magalhães <joamag@hive.pt>
// __version__   = 1.0.0
// __revision__  = $LastChangedRevision$
// __date__      = $LastChangedDate$
// __copyright__ = Copyright (c) 2008-2014 Hive Solutions Lda.
// __license__   = GNU General Public License (GPL), Version 3

(function(jQuery) {
    jQuery.fn.ucamera = function(options) {
        // the default values for the data query
        var defaults = {};

        // sets the default options value
        var options = options ? options : {};

        // constructs the options
        var options = jQuery.extend(defaults, options);

        // sets the jquery matched object
        var matchedObject = this;

        /**
         * Initializer of the plugin, runs the necessary functions to initialize
         * the structures.
         */
        var initialize = function() {
            _appendHtml();
            _registerHandlers();
        };

        /**
         * Creates the necessary html for the component.
         */
        var _appendHtml = function() {
            // retrieves the reference to the camera as the
            // currently matched object
            var camera = matchedObject;

            // retrieves the currently set camera dimensions (parsing them
            // as integer values) and sets them in the camera element (backup)
            var cameraWidth = parseInt(camera.attr("width"));
            var cameraHeight = parseInt(camera.attr("height"));
            camera.data("width", cameraWidth);
            camera.data("height", cameraHeight);
        };

        /**
         * Registers the event handlers for the created objects.
         */
        var _registerHandlers = function() {
            // retrieves the reference to the global window element
            // to be used in the key handing registration
            var _window = jQuery(window);

            // sets the camera element as the currently matched object
            // (data reference)
            var camera = matchedObject;

            // create a custom mazimize function with a clojure in the
            // camera element reference
            var __maximize = function() {
                _maximize(camera);
            };

            // creates the custom fixed scroll function that ensures that
            // the scroll top position of the window is always zero
            var __fixedScroll = function() {
                _window.scrollTop(0);
            };

            // registers for the load event on the camera so that if the
            // width and height of the camera needs update it's updated
            // in accordance with the current size
            matchedObject.load(function() {
                        // retrieves the current context as the camera component
                        // and uses it to retrieve the currently set width and
                        // height to be verified
                        var camera = jQuery(this);
                        var cameraWidth = camera.data("width");
                        var cameraHeight = camera.data("height");

                        // verifies if the current values are valid and in
                        // case they're not updates them with the current
                        // visual sizes then updates the values in the camera
                        // data structure
                        cameraWidth = cameraWidth > 0
                                ? cameraWidth
                                : camera.outerWidth();
                        cameraHeight = cameraHeight > 0
                                ? cameraHeight
                                : camera.outerHeight();
                        camera.data("width", cameraWidth);
                        camera.data("height", cameraHeight);
                    });

            // registers for the key down on the window so that
            // we can handle the fullscreen trigger, note that once
            // the current object is destroyed the event is
            // unregistered to avoid double registration
            matchedObject.length
                    && _window.keydown(onKeyDown = function(event) {
                        // retrieves the key value
                        var keyValue = event.keyCode
                                ? event.keyCode
                                : event.charCode ? event.charCode : event.which;

                        if (event.shiftKey && keyValue == 70) {
                            var maximized = camera.data("maximized") || false;
                            if (maximized) {
                                _minimize(camera);
                                _window.unbind("resize", __maximize)
                                _window.unbind("scroll", __fixedScroll);
                                camera.data("maximized", false);
                            } else {
                                _maximize(camera);
                                _window.resize(__maximize);
                                _window.scroll(__fixedScroll);
                                camera.data("maximized", true);
                            }
                        }
                    });
            matchedObject.bind("destroyed", function() {
                        _window.unbind("keydown", onKeyDown);
                    });
        };

        /**
         * Maximizes the current camera image occupying the complete screen,
         * this shiould provide a fullscreen feel.
         *
         * @param {Element}
         *            camera The reference to the camera element to be used in
         *            the maximization process.
         */
        var _maximize = function(camera) {
            // retrieves the various elements to be used in the
            // maximization operation (some of them are global)
            var _window = jQuery(window);
            var _html = jQuery("html");
            var _body = jQuery("body");
            var overlay = jQuery("#overlay");

            // resets the html element to remove all the possible
            // extra width and height from it
            _html.css("overflow-y", "hidden");
            _body.css("margin", "0px 0px 0px 0px");
            _body.css("padding", "0px 0px 0px 0px");

            // retrieves the current window height and width
            // note that this retrieval only occurs after the
            // reset fo the html element
            var windowHeight = _window.height();
            var windowWidth = _window.width();

            // retrieves the (original) camera height and with
            // to be able to calculate the aspect ratio
            var cameraHeight = camera.data("height");
            var cameraWidth = camera.data("width");

            // updates the camera position and margins to update
            // it to a fullscreen view
            camera.css("margin", "0px 0px 0px 0px");
            camera.css("position", "absolute");
            camera.css("top", "0px");
            camera.css("left", "0px");

            // calculates the aspect ratios for both the window
            // and the (original) camera dimensions
            var ratioWindow = windowWidth / windowHeight;
            var ratioCamera = cameraWidth / cameraHeight;

            // re-calculates the aspect ratio for the camera taking
            // into account the ratio of the window
            ratioCamera = ratioWindow < ratioCamera ? 0.1 : ratioCamera;

            // in case the ratio of the camera is less than one the
            // with is the "biggest" so it remain as the driver
            if (ratioCamera < 1) {
                // calculates the ratio of the resizing using the
                // window width and the camera width and then uses
                // it to calculate the new camera height
                var sizeRatio = windowWidth / cameraWidth;
                camera.width(windowWidth);
                camera.height(cameraHeight * sizeRatio);
            }
            // othewrise the height is the driver (because it's)
            // the biggest value
            else {
                // calculates the ratio of the resizing using the
                // window height and the camera height and then uses
                // it to calculate the new camera width
                var sizeRatio = windowHeight / cameraHeight;
                camera.width(cameraWidth * sizeRatio);
                camera.height(windowHeight);
            }

            // updates the z index value of the camera to the
            // maximum possible one so that it stays on top of
            // every other component in the screen
            camera.css("z-index", "99999");

            // scrolls the window to the top position so that
            // the camera is correctly viewed
            _window.scrollTop(0);

            // updates the overlay size and color (black for image
            // contrast)
            overlay.height(windowHeight);
            overlay.width(windowWidth);
            overlay.css("background", "#000000");
            overlay.css("opacity", "1.0");
            overlay.show();

            // centers the camera window on the screen to provide
            // the "normal" fullscreen screen
            camera.uxcenter();
        };

        /**
         * Minimizes the current camera image window into the "normal" behaviour
         * this function should be able to restore the original values for the
         * global elements used in a maximization. *
         *
         * @param {Element}
         *            camera The reference to the camera element to be used in
         *            the minimization process.
         */
        var _minimize = function(camera) {
            // retrieves the various elements that are going
            // to be used in the restore operation (minimization)
            var _html = jQuery("html");
            var _body = jQuery("body");
            var overlay = jQuery("#overlay");

            // resets the global attributes for the html
            // and the body elements (removes them)
            _html.css("overflow-y", null);
            _body.css("margin", null);
            _body.css("padding", null);

            // retrieves the original dimenstions of the camera
            // to restore them in the attributes
            var cameraHeight = camera.data("height");
            var cameraWidth = camera.data("width");

            // resets the camera style to avoid any extra width
            // or height into it (or event margins)
            camera.css("margin", null);
            camera.css("position", null);
            camera.css("top", null);
            camera.css("left", null);
            camera.css("z-index", null);

            // sets the original dimentsions on the camera, resets
            // its values (to the original values)
            camera.width(cameraWidth);
            camera.height(cameraHeight);

            // removes the background and opacity from the overlay
            // and hides it avoid any more display of it
            overlay.css("background", null);
            overlay.css("opacity", null);
            overlay.hide();
        };

        // initializes the plugin
        initialize();

        // returns the object
        return this;
    };
})(jQuery);

(function(jQuery) {
    jQuery.fn.ureload = function(options) {
        // the default values for the data query
        var defaults = {};

        // sets the default options value
        var options = options ? options : {};

        // constructs the options
        var options = jQuery.extend(defaults, options);

        // sets the jquery matched object
        var matchedObject = this;

        /**
         * Initializer of the plugin, runs the necessary functions to initialize
         * the structures.
         */
        var initialize = function() {
            _appendHtml();
            _registerHandlers();
        };

        /**
         * Creates the necessary html for the component.
         */
        var _appendHtml = function() {
            // in case there's no selected elements must
            // return immediately no reload
            if (matchedObject.length == 0) {
                return;
            }

            // retrieves the global reference to the body element
            // that is going to be used to "store" global information
            var _body = jQuery("body");

            // tries to retrieve a previously registered interval
            // for the reloading of the current structure and in
            // case it already exists clear it in order to avoid
            // any kind of doubl registration (would create issues)
            var interval = _body.data("interval");
            if (interval) {
                clearInterval(interval);
            }

            // retrieves the timetout information from the
            // matched object and parses it as an integer
            var timeout = matchedObject.attr("data-timeout");
            timeout = parseInt(timeout);

            // registers for the reload of the page for every
            // timeout that has passed (in case no connection
            // is available no refresh is done)
            interval = setInterval(function() {
                        _update();
                    }, timeout);
            _body.data("interval", interval);
        };

        /**
         * Registers the event handlers for the created objects.
         */
        var _registerHandlers = function() {
        };

        var _update = function() {
            // runs the remote request on the current document url
            // to make sure the connection is available before refresh
            jQuery.ajax({
                        url : document.URL,
                        success : function(data, status) {
                            // in case no data is retrieved, the server is
                            // considered to be down and (returns immediately)
                            if (!data) {
                                return;
                            }

                            // in case the status of the received message is not the
                            // correct one (success or not modified) the message is
                            // considered invalid (returns immediately)
                            if (status != "success" && status != "notmodified") {
                                return;
                            }

                            // reloads the current location to provide the interface
                            // with the must uptodate data
                            location.reload(true);
                        }
                    });
        };

        // initializes the plugin
        initialize();

        // returns the object
        return this;
    };
})(jQuery);

(function(jQuery) {
    jQuery.fn.uapply = function(options) {
        // sets the jquery matched object
        var matchedObject = this;

        // registers the camera object in the target elements
        // (should enable normal functionality)
        jQuery(".cameras img.single", matchedObject).ucamera();

        // registers for the reload operations in the target elements
        // (should reload page from time to time)
        jQuery(".reload", matchedObject).ureload();
    };
})(jQuery);

jQuery(document).ready(function() {
            var _body = jQuery("body");
            _body.bind("applied", function(event, base) {
                        base.uapply();
                    });
        });
