{% extends "partials/layout_device.html.tpl" %}
{% block title %}Devices{% endblock %}
{% block name %}Devices :: {{ device.name }}{% endblock %}
{% block style %}border-box{% endblock %}
{% block content %}
    <form action="{{ url_for('update_device', device_id = device.device_id) }}" method="post" class="form">
        <div class="label">
            <label>Device ID</label>
        </div>
        <div class="input">
            <input type="text" class="text-field" name="device_id" placeholder="eg: cam_xz" value="{{ device.device_id|unset }}"
                   data-disabled="1" data-error="{{ errors.device_id }}" />
        </div>
        <div class="label">
            <label>Type</label>
        </div>
        <div class="input">
            <input type="text" class="text-field" name="type" placeholder="eg: axis" value="{{ device.type|unset }}"
                   data-error="{{ errors.type }}" />
        </div>
        <div class="label">
            <label>Model</label>
        </div>
        <div class="input">
            <input type="text" class="text-field" name="model_d" placeholder="eg: 211" value="{{ device.model_d|unset }}"
                   data-error="{{ errors.model_d }}" />
        </div>
        <div class="label">
            <label>Device</label>
        </div>
        <div class="input">
            <div name="device" class="drop-field drop-field-select" value="{{ device.device|unset('camera') }}"
                 data-error="{{ errors.device }}">
                <ul class="data-source" data-type="local">
                    <li>camera</li>
                    <li>encoder</li>
                </ul>
            </div>
        </div>
        <div class="label">
            <label>Filtering</label>
        </div>
        <div class="input">
            <input type="hidden" name="filter_options" value="" />
            <div class="option">
                <span class="option-key">Filter <strong>resolution</strong> setting ?</span>
                {% if "resolution" in device.filter_options %}
                    <input class="option-value" type="checkbox" name="filter_options"
                           value="resolution" checked="1" />
                {% else %}
                    <input class="option-value" type="checkbox" name="filter_options"
                           value="resolution" />
                {% endif %}
            </div>
            <div class="option">
                <span class="option-key">Filter <strong>compression</strong> setting ?</span>
                {% if "compression" in device.filter_options %}
                    <input class="option-value" type="checkbox" name="filter_options"
                           value="compression" checked="1" />
                {% else %}
                    <input class="option-value" type="checkbox" name="filter_options"
                           value="compression" />
                {% endif %}
            </div>
            <div class="option">
                <span class="option-key">Filter <strong>fps</strong> setting ?</span>
                {% if "fps" in device.filter_options %}
                    <input class="option-value" type="checkbox" name="filter_options"
                           value="fps" checked="1" />
                {% else %}
                    <input class="option-value" type="checkbox" name="filter_options"
                           value="fps" />
                {% endif %}
            </div>
            <div class="option">
                <span class="option-key">Filter <strong>clock</strong> setting ?</span>
                {% if "clock" in device.filter_options %}
                    <input class="option-value" type="checkbox" name="filter_options"
                           value="clock" checked="1" />
                {% else %}
                    <input class="option-value" type="checkbox" name="filter_options"
                           value="clock" />
                {% endif %}
            </div>
        </div>
        <div class="label">
            <label>Resolution</label>
        </div>
        <div class="input">
            <input type="text" class="text-field" name="resolution" placeholder="eg: 640x480" value="{{ device.resolution|unset }}"
                   data-error="{{ errors.resolution }}" />
        </div>
        <div class="label">
            <label>Width</label>
        </div>
        <div class="input">
            <input type="text" class="text-field" name="width" placeholder="eg: 640" value="{{ device.width|unset }}"
                   data-error="{{ errors.width }}" />
        </div>
        <div class="label">
            <label>Height</label>
        </div>
        <div class="input">
            <input type="text" class="text-field" name="height" placeholder="eg: 480" value="{{ device.height|unset }}"
                   data-error="{{ errors.height }}" />
        </div>
        <div class="label">
            <label>Compression</label>
        </div>
        <div class="input">
            <input type="text" class="text-field" name="compression" placeholder="eg: 20" value="{{ device.compression|unset }}"
                   data-error="{{ errors.compression }}" />
        </div>
        <div class="label">
            <label>FPS</label>
        </div>
        <div class="input">
            <input type="text" class="text-field" name="fps" placeholder="eg: 20" value="{{ device.fps|unset }}"
                   data-error="{{ errors.fps }}" />
        </div>
        <div class="label">
            <label>Clock</label>
        </div>
        <div class="input">
            <input type="text" class="text-field" name="clock" placeholder="eg: 0" value="{{ device.clock|unset }}"
                   data-error="{{ errors.clock }}" />
        </div>
        <span class="button" data-link="{{ url_for('show_device', device_id = device.device_id) }}">Cancel</span>
        //
        <span class="button" data-submit="true">Update</span>
    </form>
{% endblock %}
