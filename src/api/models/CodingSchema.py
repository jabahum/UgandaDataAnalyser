class CodingSchema(Schema):
	system = fields.Str()
	code = fields.Str()
	@post_load
	def make_coding(self, data, **kwargs):
		return Coding(**data)