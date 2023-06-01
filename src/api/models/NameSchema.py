class NameSchema(Schema):
	id = fields.Str()
	use = fields.Str()
	family = fields.Str()
	given = fields.List(fields.Str())
	@post_load
	def make_name(self, data, **kwargs):
		return Name(**data)