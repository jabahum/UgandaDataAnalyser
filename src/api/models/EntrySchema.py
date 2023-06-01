class EntrySchema(Schema):
	fullurl = fields.Str()
	resource = fields.Nested(ResourceSchema())
	search = fields.Nested(SearchSchema())
	@post_load
	def make_entry(self, data, **kwargs):
		return Entry(**data)