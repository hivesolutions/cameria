{% include "partials/doctype.html.tpl" %}
<head>
    {% block head %}
        {% include "partials/content_type.html.tpl" %}
        {% include "partials/includes.html.tpl" %}
        <title>Cameria / {% block title %}{% endblock %}</title>
    {% endblock %}
</head>
<body class="ux full">
	<div id="overlay"></div>
    <div id="header">
        {% block header %}
            <h1>{% block name %}{% endblock %}</h1>
            <div class="links">
                {% if link == "home" %}
                    <a href="{{ url_for('index') }}" class="active">home</a>
                {% else %}
                    <a href="{{ url_for('index') }}">home</a>
                {% endif %}
                //
                {% if link == "sets" %}
                    <a href="{{ url_for('list_set') }}" class="active">sets</a>
                {% else %}
                    <a href="{{ url_for('list_set') }}">sets</a>
                {% endif %}
                //
                {% if link == "cameras" %}
                    <a href="{{ url_for('list_camera') }}" class="active">cameras</a>
                {% else %}
                    <a href="{{ url_for('list_camera') }}">cameras</a>
                {% endif %}
                //
                {% if link == "devices" %}
                    <a href="{{ url_for('list_device') }}" class="active">devices</a>
                {% else %}
                    <a href="{{ url_for('list_device') }}">devices</a>
                {% endif %}
                //
                {% if link == "about" %}
                    <a href="{{ url_for('about') }}" class="active">about</a>
                {% else %}
                    <a href="{{ url_for('about') }}">about</a>
                {% endif %}
            </div>
        {% endblock %}
    </div>
    <div id="content">{% block content %}{% endblock %}</div>
    {% include "partials/footer.html.tpl" %}
</body>
{% include "partials/end_doctype.html.tpl" %}
