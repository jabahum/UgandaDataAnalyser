class IdentifierSchema2(Schema):
	id = fields.Str()
	extension = fields.List(fields.Nested(ExtensionSchema()))
	use = fields.Str()
	type = fields.Nested(TypeSchema())
	system = fields.Str()
	value = fields.Str()
	@post_load
	def make_identifier(self, data, **kwargs):
		return Identifier(**data)