class SearchSchema(Schema):
	mode = fields.Str()
	@post_load
	def make_search(self, data, **kwargs):
		return Search(**data)