class ValuereferenceSchema(Schema):
	reference = fields.Str()
	type = fields.Str()
	display = fields.Str()
	@post_load
	def make_valuereference(self, data, **kwargs):
		return Valuereference(**data)