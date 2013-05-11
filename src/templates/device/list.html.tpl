{% extends "partials/layout_device_l.html.tpl" %}
{% block title %}Devices{% endblock %}
{% block name %}Devices{% endblock %}
{% block content %}
    <ul class="filter" data-infinite="1" data-no_input="1">
        <div class="data-source" data-url="{{ url_for('list_devices_json') }}" data-type="json" data-timeout="0"></div>
        <li class="template">
            <div class="name">
                <a href="{{ url_for('show_device', device_id = '') }}%[device_id]">%[name]</a>
            </div>
        </li>
        <div class="filter-no-results quote">
            No results found
        </div>
        <div class="filter-more">
            <span class="button more">Load more</span>
            <span class="button load">Loading</span>
        </div>
    </ul>
{% endblock %}
