class LinkSchema2(Schema):
	relation = fields.Str()
	url = fields.Str()
	@post_load
	def make_link(self, data, **kwargs):
		return Link(**data)