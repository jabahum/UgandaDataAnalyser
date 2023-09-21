class TagSchema(Schema):
	system = fields.Str()
	code = fields.Str()
	display = fields.Str()
	@post_load
	def make_tag(self, data, **kwargs):
		return Tag(**data)