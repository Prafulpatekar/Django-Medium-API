import json

from rest_framework.renderers import JSONRenderer


class ArticleJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = 200
        if renderer_context is not None:
            status_code = renderer_context["response"].status_code

        errors = None
        if data is not None:
            errors = data.get("errors", None)
            
        if errors is not None:
            return super(ArticleJSONRenderer, self).render(data)

        return json.dumps({"status_code": status_code, "article": data})


class ArticlesJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code

        errors = data.get("errors", None)

        if errors is not None:
            return super(ArticlesJSONRenderer, self).render(data)

        return json.dumps({"status_code": status_code, "articles": data})