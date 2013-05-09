{% extends "partials/layout_device.html.tpl" %}
{% block title %}Devices{% endblock %}
{% block name %}Devices :: {{ device.device_id }}{% endblock %}
{% block content %}
    <form action="{{ url_for('update_device', device_id = device.device_id) }}" method="post" class="form">
        <div class="label">
            <label>Device ID</label>
        </div>
        <div class="input">
            <input class="text-field focus" name="device_id" placeholder="eg: cam_xz" value="{{ device.device_id }}"
                   data-disabled="1" data-error="{{ errors.device_id }}" />
        </div>
        <div class="label">
            <label>Type</label>
        </div>
        <div class="input">
            <input class="text-field" name="type" placeholder="eg: axis" value="{{ device.type }}"
                   data-error="{{ errors.type }}" />
        </div>
        <div class="label">
            <label>Model</label>
        </div>
        <div class="input">
            <input class="text-field" name="model_d" placeholder="eg: 211" value="{{ device.model_d }}"
                   data-error="{{ errors.model_d }}" />
        </div>
        <div class="label">
            <label>Device</label>
        </div>
        <div class="input">
            <div name="device" class="drop-field drop-field-select" value="{{ device.device | default('camera') }}"
                 data-error="{{ errors.device }}">
                <ul class="data-source" data-type="local">
                    <li>camera</li>
                    <li>encoder</li>
                </ul>
            </div>
        </div>
        <div class="label">
            <label>Random</label>
        </div>
        <div class="input">
            <div class="option">
                <span class="float-left">Provide resolution support ?</span>
                {%if device.has_resolution %}
                    <input class="float-right" type="checkbox" name="has_resolution" checked="1" />
                {% else %}
                    <input class="float-right" type="checkbox" name="has_resolution" />
                {% endif %}
                <div class="clear"></div>
            </div>
        </div>
        <div class="label">
            <label>Resolution</label>
        </div>
        <div class="input">
            <input class="text-field" name="resolution" placeholder="eg: 640x480" value="{{ device.resolution }}"
                   data-error="{{ errors.resolution }}" />
        </div>
        <div class="label">
            <label>Width</label>
        </div>
        <div class="input">
            <input class="text-field" name="width" placeholder="eg: 640" value="{{ device.width }}"
                   data-error="{{ errors.width }}" />
        </div>
        <div class="label">
            <label>Height</label>
        </div>
        <div class="input">
            <input class="text-field" name="height" placeholder="eg: 480" value="{{ device.height }}"
                   data-error="{{ errors.height }}" />
        </div>
        <div class="label">
            <label>Compression</label>
        </div>
        <div class="input">
            <input class="text-field" name="compression" placeholder="eg: 20" value="{{ device.compression }}"
                   data-error="{{ errors.compression }}" />
        </div>
        <div class="label">
            <label>Fps</label>
        </div>
        <div class="input">
            <input class="text-field" name="fps" placeholder="eg: 20" value="{{ device.fps }}"
                   data-error="{{ errors.fps }}" />
        </div>
        <div class="label">
            <label>Clock</label>
        </div>
        <div class="input">
            <input class="text-field" name="clock" placeholder="eg: 0" value="{{ device.clock }}"
                   data-error="{{ errors.clock }}" />
        </div>
        <span class="button" data-link="{{ url_for('show_device', device_id = device.device_id) }}">Cancel</span>
        //
        <span class="button" data-submit="true">Update</span>
    </form>
{% endblock %}