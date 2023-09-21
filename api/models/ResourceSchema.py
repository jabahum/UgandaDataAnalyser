class ResourceSchema(Schema):
	resourcetype = fields.Str()
	id = fields.Str()
	meta = fields.Nested(MetaSchema())
	text = fields.Nested(TextSchema())
	identifier = fields.List(fields.Nested(IdentifierSchema()))
	active = fields.Boolean()
	name = fields.List(fields.Nested(NameSchema()))
	telecom = fields.List(fields.Nested(TelecomSchema()))
	gender = fields.Str()
	birthdate = fields.Str()
	deceasedboolean = fields.Boolean()
	address = fields.List(fields.Nested(AddressSchema()))
	managingorganization = fields.Nested(ManagingorganizationSchema())
	link = fields.List(fields.Nested(LinkSchema()))
	@post_load
	def make_resource(self, data, **kwargs):
		return Resource(**data)