class LinkSchema(Schema):
	other = fields.Nested(OtherSchema())
	type = fields.Str()
	@post_load
	def make_link(self, data, **kwargs):
		return Link(**data)