class MetaSchema2(Schema):
	lastupdated = fields.Str()
	@post_load
	def make_meta(self, data, **kwargs):
		return Meta(**data)