{% extends "partials/layout_camera_l.html.tpl" %}
{% block title %}Cameras{% endblock %}
{% block name %}{{ camera.id }} :: edit{% endblock %}
{% block content %}
    <form action="{{ url_for('create_camera') }}" method="post" class="form">
        <div class="label">
            <label>Camera ID</label>
        </div>
        <div class="input">
            <input class="text-field focus" name="camera_id" placeholder="eg: cam_xz" value="{{ camera.camera_id }}"
                   data-disabled="1" data-error="{{ errors.camera_id }}" />
        </div>
        <div class="label">
            <label>URL</label>
        </div>
        <div class="input">
            <input class="text-field" name="url" placeholder="eg: http://cameria.com/cam_xz" value="{{ camera.url }}"
                   data-error="{{ camera.url }}" />
        </div>
        <div class="label">
            <label>Camera</label>
        </div>
        <div class="input">
            <input class="text-field" name="camera" placeholder="eg: 1" value="{{ camera.camera }}"
                   data-error="{{ camera.camera }}" />
        </div>
        <div class="label">
            <label>Username</label>
        </div>
        <div class="input">
            <input class="text-field" name="username" placeholder="eg: johndoe" value="{{ camera.username }}"
                   data-error="{{ camera.username }}" />
        </div>
        <div class="label">
            <label>Password</label>
        </div>
        <div class="input">
            <input type="password" class="text-field" name="password" value="{{ camera.password }}"
                   data-error="{{ camera.password }}" />
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
                   data-error="{{ camera.compression }}" />
        </div>
        <div class="label">
            <label>FPS</label>
        </div>
        <div class="input">
            <input class="text-field" name="fps" placeholder="eg: 4" value="{{ camera.fps }}"
                   data-error="{{ camera.fps }}" />
        </div>
        <div class="label">
            <label>Type</label>
        </div>
        <div class="input">
            <input class="text-field" name="type" placeholder="eg: axis" value="{{ camera.type }}"
                   data-error="{{ camera.type }}" />
        </div>
        <div class="label">
            <label>Model</label>
        </div>
        <div class="input">
            <input class="text-field" name="model_" placeholder="eg: m1114" value="{{ camera.model_ }}"
                   data-error="{{ camera.model_ }}" />
        </div>
        <div class="label">
            <label>Description</label>
        </div>
        <div class="input">
            <textarea class="text-area" name="description" placeholder="eg: some words about the camera"
                      data-error="{{ camera.description }}">{{ camera.description }}</textarea>
        </div>
        <div class="quote">
            By clicking Submit Camera, you agree to our Service Agreement and that you have
            read and understand our Privacy Policy.
        </div>
        <span class="button" data-submit="true">Submit Camera</span>
    </form>
{% endblock %}
