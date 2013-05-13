{% extends "partials/layout_settings.html.tpl" %}
{% block title %}Settings{% endblock %}
{% block name %}Settings{% endblock %}
{% block content %}
    <ul>
        <li>
            <div class="name"><a href="{{ url_for('import_a') }}">Import</a></div>
            <div class="description"><span>Import data from a database file</span></div>
        </li>
        <li>
            <div class="name"><a href="{{ url_for('export_do') }}">Export</a></div>
            <div class="description"><span>Export your current database into an external file</span></div>
        </li>
    </ul>
{% endblock %}
