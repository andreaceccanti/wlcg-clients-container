FROM centos:7

# Allow customization of test user ID
ARG TEST_USER_UID=501

ENV TEST_USER test
ENV TEST_USER_UID $TEST_USER_UID

RUN echo "include_only=.garr.it,.cern.ch" >> /etc/yum/pluginconf.d/fastestmirror.conf && \
      yum clean all && \
      yum install -y hostname epel-release && \
      yum -y update && \
      yum -y install which wget tar sudo file && \
      echo '%wheel ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
      adduser --uid ${TEST_USER_UID} ${TEST_USER} && \
      usermod -a -G wheel ${TEST_USER} && \
      mkdir /home/test/.config && chown test:test /home/test/.config && \
      yum -y install telnet nc

RUN wget https://ci.cloud.cnaf.infn.it/view/repos/job/repo_test_ca/lastSuccessfulBuild/artifact/test-ca.repo -O /etc/yum.repos.d/test-ca.repo && \
    yum -y clean all && yum -y install igi-test-ca && \
    mkdir -p /home/test/.globus && cp /usr/share/igi-test-ca/test0.p12 /home/test/.globus/usercred.p12 && \
    chmod 600 /home/test/.globus/usercred.p12 && \
    chown -R test:test /home/test/.globus

RUN wget https://fts-repo.web.cern.ch/fts-repo/fts3-rc-el7.repo -O /etc/yum.repos.d/fts3-rc-el7.repo && \
    wget https://dmc-repo.web.cern.ch/dmc-repo/dmc-rc-el7.repo -O /etc/yum.repos.d/dmc-rc-el7.repo 

RUN yum -y install epel-release && \
    yum -y install voms-clients-java gfal2-util gfal2-all gfal2-python jq davix fts-client && \
    yum clean all && \
    rm -rf /var/cache/yum

RUN yum -y install https://github.com/indigo-dc/oidc-agent/releases/download/v3.3.5/oidc-agent-3.3.5-1.el7.x86_64.rpm

ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

USER test
WORKDIR /home/test
