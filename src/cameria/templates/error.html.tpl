{% extends "partials/layout_simple.html.tpl" %}
{% block title %}Error{% endblock %}
{% block name %}Error{% endblock %}
{% block content %}
    <div class="quote">
        There was an problem while executing an operation.<br />
        Please contact the <strong>system administrator</strong> for more information.
    </div>
    <div class="separator-horizontal"></div>
    {% if error %}
        <div class="quote error">{{ error }}</div>
    {% endif %}
    {% if traceback %}
        <div class="quote">
            <a class="link replacer" data-target=".traceback" data-no_auto="1">show traceback</a>
           </div>
        <ul class="traceback replacer-target">
            {% for line in traceback %}
                <li>{{ line }}</li>
            {% endfor %}
        </ul>
    {% endif %}
{% endblock %}
