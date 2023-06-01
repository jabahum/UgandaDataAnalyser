class ExtensionSchema2(Schema):
	url = fields.Str()
	valuereference = fields.Nested(ValuereferenceSchema())
	@post_load
	def make_extension(self, data, **kwargs):
		return Extension(**data)