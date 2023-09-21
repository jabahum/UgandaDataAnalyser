class ExtensionSchema(Schema):
	url = fields.Str()
	extension = fields.List(fields.Nested(ExtensionSchema()))
	@post_load
	def make_extension(self, data, **kwargs):
		return Extension(**data)