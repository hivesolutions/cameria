{% extends "partials/layout_camera_l.html.tpl" %}
{% block title %}Cameras{% endblock %}
{% block name %}Cameras{% endblock %}
{% block content %}
    <ul class="filter" data-infinite="1" data-no_input="1">
        <div class="data-source" data-url="{{ url_for('list_cameras_json') }}" data-type="json" data-timeout="0"></div>
        <li class="template">
            <div class="name">
                <a href="{{ url_for('show_camera', camera_id = '') }}%[camera_id]">%[camera_id]</a>
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
