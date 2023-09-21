class IdentifierSchema(Schema):
	use = fields.Str()
	system = fields.Str()
	value = fields.Str()
	@post_load
	def make_identifier(self, data, **kwargs):
		return Identifier(**data)