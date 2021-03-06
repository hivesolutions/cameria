{% extends "partials/layout_camera.html.tpl" %}
{% block title %}Cameras{% endblock %}
{% block name %}Cameras :: {{ camera.camera_id }}{% endblock %}
{% block style %}border-box{% endblock %}
{% block content %}
    <form action="{{ url_for('update_camera', camera_id = camera.camera_id) }}" method="post" class="form">
        <div class="label">
            <label>Camera ID</label>
        </div>
        <div class="input">
            <input type="text" class="text-field" name="camera_id" placeholder="eg: cam_xz" value="{{ camera.camera_id|unset }}"
                   data-disabled="1" data-error="{{ errors.camera_id }}" />
        </div>
        <div class="label">
            <label>URL</label>
        </div>
        <div class="input">
            <input type="text" class="text-field" name="url" placeholder="eg: http://cameria.com/cam_xz" value="{{ camera.url|unset }}"
                   data-error="{{ errors.url }}" />
        </div>
        <div class="label">
            <label>Camera</label>
        </div>
        <div class="input">
            <input type="text" class="text-field" name="camera" placeholder="eg: 1" value="{{ camera.camera|unset }}"
                   data-error="{{ errors.camera }}" />
        </div>
        <div class="label">
            <label>Username</label>
        </div>
        <div class="input">
            <input type="text" class="text-field" name="username" placeholder="eg: johndoe" value="{{ camera.username|unset }}"
                   data-error="{{ errors.username }}" />
        </div>
        <div class="label">
            <label>Password</label>
        </div>
        <div class="input">
            <input type="password" class="text-field" name="password" value="{{ camera.password|unset }}"
                   data-error="{{ errors.password }}" />
        </div>
        <div class="label">
            <label>Protocol</label>
        </div>
        <div class="input">
            <div name="protocol" class="drop-field drop-field-select" value="{{ camera.protocol|unset('http') }}"
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
            <input type="text" class="text-field" name="compression" placeholder="eg: 30" value="{{ camera.compression|unset }}"
                   data-error="{{ errors.compression }}" />
        </div>
        <div class="label">
            <label>FPS</label>
        </div>
        <div class="input">
            <input type="text" class="text-field" name="fps" placeholder="eg: 4" value="{{ camera.fps|unset }}"
                   data-error="{{ errors.fps }}" />
        </div>
        <div class="label">
            <label>Device</label>
        </div>
        <div class="input">
            <div class="input">
                <div class="drop-field" value="{{ camera.device.name|unset }}" placeholder="eg: axis m1114"
                     data-display_attribute="name" data-value_attribute="device_id" data-error="{{ errors.device }}">
                    <input name="device" type="hidden" class="hidden-field" value="{{ camera.device.device_id }}" />
                    <ul class="data-source" data-url="{{ url_for('list_devices_json') }}"
                        data-type="json"></ul>
                </div>
            </div>
        </div>
        <span class="button" data-link="{{ url_for('show_camera', camera_id = camera.camera_id) }}">Cancel</span>
        //
        <span class="button" data-submit="true">Update</span>
    </form>
{% endblock %}
