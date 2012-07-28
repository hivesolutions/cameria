// Hive Cameria System
// Copyright (C) 2008-2012 Hive Solutions Lda.
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
// __copyright__ = Copyright (c) 2010-2012 Hive Solutions Lda.
// __license__   = GNU General Public License (GPL), Version 3

(function($) {
    jQuery.fn.uxcamera = function(options) {
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

            // registers for the key down on the window so that
            // we can handle the fullscreen trigger
            matchedObject.length && _window.keydown(function(event) {
                        // retrieves the key value
                        var keyValue = event.keyCode
                                ? event.keyCode
                                : event.charCode ? event.charCode : event.which;

                        if (event.shiftKey && keyValue == 70) {
                            var maximized = camera.data("maximized") || false;
                            if (maximized) {
                                _minimize(camera);
                                _window.unbind("resize", __maximize)
                                camera.data("maximized", false);
                            } else {
                                _maximize(camera);
                                _window.resize(__maximize);
                                camera.data("maximized", true);
                            }
                        }
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

            // updates the overlay size and color (black for image
            // contrast)
            overlay.height(windowHeight);
            overlay.width(windowWidth);
            overlay.css("background", "#000000");
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

            // sets the original dimentsions on the camera, resets
            // its values (to the original values)
            camera.width(cameraWidth);
            camera.height(cameraHeight);

            // removes the background from the overlay and hides
            // it avoid any more display of it
            overlay.css("background", null);
            overlay.hide();
        };

        // initializes the plugin
        initialize();

        // returns the object
        return this;
    };
})(jQuery);

jQuery(document).ready(function() {
            // registers the camera object in the target elements
            // (should enalbe normal functionality)
            jQuery(".cameras img.single").uxcamera();
        });
