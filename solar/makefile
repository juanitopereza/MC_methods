grafica.pdf: parametros.dat simple_matplotlib.py
	python simple_matplotlib.py

parametros.dat: mcmc_solar.x
	./mcmc_solar.x 10000 1000 > parametros.dat

mcmc_solar.x: solar.c datos_f.dat datos_t.dat
	cc solar.c -lm -o mcmc_solar.x

datos_f.dat datos_t.dat: dat_filter.py monthrg.dat
	python dat_filter.py

clean:
	rm -f mcmc_solar.x datos_f.dat datos_t.dat parametros.dat

