class TelecomSchema(Schema):
	id = fields.Str()
	value = fields.Str()
	@post_load
	def make_telecom(self, data, **kwargs):
		return Telecom(**data)