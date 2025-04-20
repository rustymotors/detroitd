FROM node:23

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

# Add Tini
ENV TINI_VERSION=v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

WORKDIR /home/node/app

COPY --chown=node:node package*.json ./

USER node


RUN npm install
COPY --chown=node:node . .

EXPOSE 8080

CMD ["node", "app.ts" ]