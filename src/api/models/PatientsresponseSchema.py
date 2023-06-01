class PatientsresponseSchema(Schema):
	resourcetype = fields.Str()
	id = fields.Str()
	meta = fields.Nested(MetaSchema())
	type = fields.Str()
	total = fields.Int()
	link = fields.List(fields.Nested(LinkSchema()))
	entry = fields.List(fields.Nested(EntrySchema()))
	@post_load
	def make_patientsresponse(self, data, **kwargs):
		return Patientsresponse(**data)

    