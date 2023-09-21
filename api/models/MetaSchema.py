class MetaSchema(Schema):
	versionid = fields.Str()
	lastupdated = fields.Str()
	source = fields.Str()
	tag = fields.List(fields.Nested(TagSchema()))
	@post_load
	def make_meta(self, data, **kwargs):
		return Meta(**data)