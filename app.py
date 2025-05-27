from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the item', required=True)
parser.add_argument('color', type=str, help='Color of the item', required=True)

parser_put = reqparse.RequestParser()
parser_put.add_argument('name', type=str, help='Name of the item')
parser_put.add_argument('color', type=str, help='Color of the item')



items = {
	1 : {'name':'item1', 'color' : 'red'},
	2 : {'name':'item2', 'color' : 'blue'},
	3 : {'name':'item3', 'color' : 'orange'}
}


class Item(Resource):
	def get(self, item_id):
		return items

	def post(self, item_id):
		args = parser.parse_args()
		if item_id in items:
			return 400
		items[item_id] = {'name' : args['name'], 'color' : args['color']}

		return 201

	def put(self, item_id):
		args = parser.parse_args()
		if item_id not in items:
			return 404
		items[item_id] = {'name' : args['name'], 'color' : args['color']}

		return 204

	def patch(self, item_id):
		args = parser_put.parse_args()
		if item_id not in items:
			return 404

		if args['name']:
			items[item_id]['name'] = args['name']
		if args['color']:
			items[item_id]['color'] = args['color']

		return items[item_id]

	def delete(self, item_id):
		if item_id not in items:
			return 404
		del items[item_id]

		return 205


api.add_resource(Item, '/items/<int:item_id>')



if __name__ == '__main__':
	app.run(debug=True, port=3000)