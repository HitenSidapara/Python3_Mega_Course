from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")


@app.route("/about/")
def about():
	return render_template("about.html")

@app.route("/map/")
def map():
	from pandas_datareader import data
	from bokeh.plotting import figure, output_file, show
	from bokeh.embed import components
	from bokeh.resources import CDN
	import datetime

	start = datetime.datetime(2015, 11, 1)
	end = datetime.datetime(2016, 3, 10)
	df = data.DataReader(name="GOOG", data_source="yahoo", start=start, end=end)

	# calculate data

	def inc_dec(c, o):
		if c > o:
			value = "Increase"
		elif o > c:
			value = "Decrease"
		else:
			value = "Equal"
		return value

	df["Status"] = [inc_dec(c, o) for c, o in zip(df["Close"], df["Open"])]
	df["Middle"] = (df.Open + df.Close) / 2
	df["Height"] = abs(df.Open - df.Close) / 2

	p = figure(x_axis_type="datetime", width=1000, height=300, title="CandleStick Chart")

	hours_12 = 12 * 60 * 60 * 1000

	p.grid.grid_line_alpha = 0.3

	p.segment(df.index, df.High, df.index, df.Low, color="Black")

	p.rect(df.index[df["Status"] == "Increase"],
		   df.Middle[df["Status"] == "Increase"],
		   hours_12, df.Height[df["Status"] == "Increase"],
		   fill_color="#CCFFFF", line_color="black")

	p.rect(df.index[df["Status"] == "Decrease"],
		   df.Middle[df["Status"] == "Decrease"],
		   hours_12, df.Height[df["Status"] == "Decrease"],
		   fill_color="#FF3333", line_color="black")

	script1, div1 = components(p)
	cdn_js = CDN.js_files[0]
	cdn_css = CDN.css_files[0]

	return render_template("map.html",script1=script1,div1=div1,cdn_js=cdn_js,cdn_css=cdn_css)


if __name__ == '__main__':
	app.run(debug=True)