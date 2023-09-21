class ManagingorganizationSchema(Schema):
	reference = fields.Str()
	type = fields.Str()
	identifier = fields.Nested(IdentifierSchema())
	display = fields.Str()
	@post_load
	def make_managingorganization(self, data, **kwargs):
		return Managingorganization(**data)