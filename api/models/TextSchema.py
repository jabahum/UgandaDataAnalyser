class TextSchema(Schema):
	status = fields.Str()
	div = fields.Str()
	@post_load
	def make_text(self, data, **kwargs):
		return Text(**data)