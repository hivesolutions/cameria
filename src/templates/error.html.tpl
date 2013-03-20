{% extends "partials/layout.html.tpl" %}
{% block title %}Error{% endblock %}
{% block name %}Error{% endblock %}
{% block content %}
    <div class="quote">
        There was an problem while executing an operation.<br />
        Please contact the <strong>system administrator</strong> for more information.
    </div>
    <div class="separator-horizontal"></div>
    <div class="quote error">
        {{ error }}
    </div>
{% endblock %}
