{% include "partials/doctype.html.tpl" %}
<head>
    {% block head %}
        {% include "partials/content_type.html.tpl" %}
        {% include "partials/includes.html.tpl" %}
        <title>Cameria / {% block title %}{% endblock %}</title>
    {% endblock %}
</head>
<body class="ux romantic full">
    <div id="overlay" class="overlay"></div>
    <div id="header">
        {% block header %}
            <h1>{% block name %}{% endblock %}</h1>
            <div class="links">
                {% if acl("index") %}
                    {% if link == "home" %}
                        <a href="{{ url_for('index') }}" class="active">home</a>
                    {% else %}
                        <a href="{{ url_for('index') }}">home</a>
                    {% endif %}
                {% endif %}
                {% if acl("sets.list") %}
                    //
                    {% if link == "sets" %}
                        <a href="{{ url_for('list_sets') }}" class="active">sets</a>
                    {% else %}
                        <a href="{{ url_for('list_sets') }}">sets</a>
                    {% endif %}
                {% endif %}
                {% if acl("cameras.list") %}
                    //
                    {% if link == "cameras" %}
                        <a href="{{ url_for('list_cameras') }}" class="active">cameras</a>
                    {% else %}
                        <a href="{{ url_for('list_cameras') }}">cameras</a>
                    {% endif %}
                {% endif %}
                {% if acl("devices.list") %}
                    //
                    {% if link == "devices" %}
                        <a href="{{ url_for('list_devices') }}" class="active">devices</a>
                    {% else %}
                        <a href="{{ url_for('list_devices') }}">devices</a>
                    {% endif %}
                {% endif %}
                {% if acl("accounts.list") %}
                    //
                    {% if link == "accounts" %}
                        <a href="{{ url_for('list_accounts') }}" class="active">accounts</a>
                    {% else %}
                        <a href="{{ url_for('list_accounts') }}">accounts</a>
                    {% endif %}
                {% endif %}
                {% if acl("settings") %}
                    //
                    {% if link == "settings" %}
                        <a href="{{ url_for('settings') }}" class="active">settings</a>
                    {% else %}
                        <a href="{{ url_for('settings') }}">settings</a>
                    {% endif %}
                {% endif %}
                {% if acl("about") %}
                    //
                    {% if link == "about" %}
                        <a href="{{ url_for('about') }}" class="active">about</a>
                    {% else %}
                        <a href="{{ url_for('about') }}">about</a>
                    {% endif %}
                {% endif %}
            </div>
        {% endblock %}
    </div>
    <div id="content">{% block content %}{% endblock %}</div>
    {% include "partials/messages.html.tpl" %}
    {% include "partials/footer.html.tpl" %}
</body>
{% include "partials/end_doctype.html.tpl" %}
