{% extends "partials/layout_camera_l.html.tpl" %}
{% block title %}Cameras{% endblock %}
{% block name %}New Camera{% endblock %}
{% block content %}
    <form action="{{ url_for('create_camera') }}" method="post" class="form">
        <div class="label">
            <label>Camera ID</label>
        </div>
        <div class="input">
            <input class="text-field focus" name="camera_id" placeholder="eg: cam_xz" value="{{ camera.camera_id }}"
                   data-error="{{ errors.camera_id }}" />
        </div>
        <div class="label">
            <label>URL</label>
        </div>
        <div class="input">
            <input class="text-field" name="url" placeholder="eg: http://cameria.com/cam_xz" value="{{ camera.url }}"
                   data-error="{{ errors.url }}" />
        </div>
        <div class="label">
            <label>Camera</label>
        </div>
        <div class="input">
            <input class="text-field" name="camera" placeholder="eg: 1" value="{{ camera.camera }}"
                   data-error="{{ errors.camera }}" />
        </div>
        <div class="label">
            <label>Username</label>
        </div>
        <div class="input">
            <input class="text-field" name="username" placeholder="eg: johndoe" value="{{ camera.username }}"
                   data-error="{{ errors.username }}" />
        </div>
        <div class="label">
            <label>Password</label>
        </div>
        <div class="input">
            <input type="password" class="text-field" name="password" value="{{ camera.password }}"
                   data-error="{{ errors.password }}" />
        </div>
        <div class="label">
            <label>Protocol</label>
        </div>
        <div class="input">
            <div name="protocol" class="drop-field drop-field-select" value="{{ camera.protocol | default('http') }}"
                 data-error="{{ errors.protocol }}">
                <ul class="data-source" data-type="local">
                    <li>http</li>
                    <li>https</li>
                </ul>
            </div>
        </div>
        <div class="label">
            <label>Compression</label>
        </div>
        <div class="input">
            <input class="text-field" name="compression" placeholder="eg: 30" value="{{ camera.compression }}"
                   data-error="{{ errors.compression }}" />
        </div>
        <div class="label">
            <label>FPS</label>
        </div>
        <div class="input">
            <input class="text-field" name="fps" placeholder="eg: 4" value="{{ camera.fps }}"
                   data-error="{{ errors.fps }}" />
        </div>
        <div class="label">
            <label>Device</label>
        </div>
        <div class="input">
            <div class="drop-field" value="{{ camera.device.name }}" placeholder="eg: axis m1114"
                 data-display_attribute="name" data-value_attribute="device_id" data-error="{{ errors.device }}">
                <input name="device" type="hidden" class="hidden-field" value="{{ camera.device.device_id }}" />
                <ul class="data-source" data-url="{{ url_for('list_devices_json') }}"
                    data-type="json"></ul>
            </div>
        </div>
        <div class="quote">
            By clicking Submit Camera, you agree to our Service Agreement and that you have
            read and understand our Privacy Policy.
        </div>
        <span class="button" data-submit="true">Submit Camera</span>
    </form>
{% endblock %}
