from dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

    def get_all_by_director(self, mid):
        with self.session.begin():
            query = self.session.query(Movie).filter(Movie.director_id == mid).all()
        return query

    def get_all_by_genre(self, mid):
        with self.session.begin():
            query = self.session.query(Movie).filter(Movie.genre_id == mid).all()
        return query

    def get_all_by_year(self, mid):
        with self.session.begin():
            query = self.session.query(Movie).filter(Movie.year == mid).all()
        return query
