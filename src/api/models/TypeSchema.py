class TypeSchema(Schema):
	coding = fields.List(fields.Nested(CodingSchema()))
	text = fields.Str()
	@post_load
	def make_type(self, data, **kwargs):
		return Type(**data)