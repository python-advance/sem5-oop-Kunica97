import unittest
import os
import app

class MyTestCase(unittest.TestCase):
	# мы проверяем работу добавления комментов на пост
	def test_post_comments_count(self):
		newPost = app.Post("","","")
		newPost.add_comment(app.Comment("","",""))
		newPost.add_comment(app.Comment("","",""))
		newPost.add_comment(app.Comment("","",""))
		newPost.add_comment(app.Comment("","",""))
		newPost.add_comment(app.Comment("","",""))
		self.assertEqual(len(newPost.get_comments()), 5)

	# мы добавляем комменты на коммент
	def test_comment_comments_count(self):
		comment = app.Comment("2","2","2")
		comment.add_comment(app.Comment("1","1","1"))
		comment.add_comment(app.Comment("1","1","1"))
		comment.add_comment(app.Comment("1","1","1"))
		comment.add_comment(app.Comment("1","1","1"))
		comment.add_comment(app.Comment("1","1","1"))
		self.assertEqual(len(comment.get_comments()), 1)

	# соответствие названия - названию
	def test_change_title(self):
		newPost = app.Post("","","")
		newPost.set_title("new-title")
		self.assertEqual(newPost.get_title(), "new-title")

	# соответствие автора - автору
	def test_change_author(self):
		newPost = app.Post("","","")
		newPost.set_author("my-name")
		self.assertEqual(newPost.get_author(), "my-name")

	# соответствие описания - описанию
	def test_change_data(self):
		newPost = app.Post("","","")
		newPost.set_data("my-data")
		self.assertEqual(newPost.get_data(), "my-data")

if __name__ == '__main__':
	unittest.main()
