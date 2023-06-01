class AddressSchema(Schema):
	id = fields.Str()
	extension = fields.List(fields.Nested(ExtensionSchema()))
	use = fields.Str()
	city = fields.Str()
	postalcode = fields.Str()
	country = fields.Str()
	@post_load
	def make_address(self, data, **kwargs):
		return Address(**data)