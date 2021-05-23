class AuthorsObjectsMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(author_id=self.request.user.id)
        return qs
