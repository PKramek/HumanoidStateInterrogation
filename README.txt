To run notebook use command:
xvfb-run -s "-screen 0 1400x900x24" jupyter notebook --allow-root --ip 0.0.0.0 --NotebookApp.token='token'

When asked for token by jupyter notebook server pass "token"