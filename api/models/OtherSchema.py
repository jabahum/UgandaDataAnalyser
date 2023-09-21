class OtherSchema(Schema):
	reference = fields.Str()
	@post_load
	def make_other(self, data, **kwargs):
		return Other(**data)