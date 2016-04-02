BookModel = Backbone.Model.extend({
	urlRoot : '/api/v1/books/'
});

BookCollection = Backbone.Collection.extend({
    model: BookModel,
    url:'/api/v1/books/'
});

var AddNewAdvertisementView = Backbone.View.extend({
  el: '#add-new-book',
  events: {
    'submit': 'submit'
  },
  submit: function(e) {
    e.preventDefault();
    var book = new BookModel({
      name: $('#book-name').val(),
      author: $('#book-author').val(),
      price: $('#book-price').val(),
    });
    book.save();
    BookCollection.add(book);

  }

});