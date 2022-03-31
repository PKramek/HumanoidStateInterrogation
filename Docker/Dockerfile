# syntax=docker/dockerfile:1
FROM tensorflow/tensorflow:2.1.0-gpu-py3

RUN apt update
RUN apt-get update

RUN apt-get install -y git wget zip libosmesa6-dev libgl1-mesa-glx libglfw3  libffi-dev patchelf xvfb

#Download ACERAC
RUN git clone https://github.com/PKramek/HumanoidStateInterrogation.git

# Install Python 3.7
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
RUN apt install -y python3.7
RUN apt install -y libpython3.7-dev
RUN apt install -y python3.7-dev
RUN apt install -y python3-wheel

# Install mujoco
RUN ln -s /usr/lib/x86_64-linux-gnu/libGL.so.1 /usr/lib/x86_64-linux-gnu/libGL.so
RUN mkdir root/.mujoco
WORKDIR root/.mujoco

RUN wget https://roboti.us/download/mujoco200_linux.zip -O mujoco.zip
RUN unzip mujoco.zip -d /root/.mujoco
RUN mv /root/.mujoco/mujoco200_linux /root/.mujoco/mujoco200
RUN rm mujoco.zip

COPY ./mjkey.txt /root/.mujoco/

WORKDIR /

ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV LD_LIBRARY_PATH /root/.mujoco/mujoco200/bin:${LD_LIBRARY_PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib64:${LD_LIBRARY_PATH}

# Install and configute virtualenv
RUN apt-get install python3.7-venv

# venv trick https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
ENV VIRTUAL_ENV=acerac-venv
RUN python3.7 -m venv acerac-venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


RUN pip install -r HumanoidStateInterrogation/requirements.txt
RUN pip install cffi==1.15.0 fasteners==0.16.3 Cython==0.29.24 glfw==2.3.0 imageio==2.10.1 wheel
RUN pip install mujoco-py==2.0.2.9 --no-cache-dir --no-binary :all: --no-build-isolation

RUN pip install jupyter

ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD /run.sh