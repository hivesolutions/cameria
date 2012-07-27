{% extends "partials/layout.html.tpl" %}
{% block title %}Sets{% endblock %}
{% block name %}Sets{% endblock %}
{% block content %}
    <ul>
        {% for set in sets %}
            <li>
                <div class="name">
                    <a href="{{ url_for('show_set', id = set.id) }}">{{ set.name }}</a>
                </div>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
