
CLI = docker-compose -f docker/compose/docker-compose-cli.yml

.PHONY: build_dev
build_dev:
	docker build -f docker/php/Dockerfile . \
	-t af.flyeralarm/newproject/php:dev
	docker build -f docker/nginx/Dockerfile . \
	-t af.flyeralarm/newproject/nginx:dev
	docker build -f docker/database/Dockerfile . \
	-t af.flyeralarm/newproject/database:dev
	docker build -f docker/php_cli/Dockerfile . \
	-t af.flyeralarm/newproject/php_cli:dev

.PHONY: run
run:
	docker-compose -f docker/compose/docker-compose-dev.yml up -d

.PHONY: stop
stop:
	docker-compose -f docker/compose/docker-compose-dev.yml down
	
.PHONY: restart
restart:
	docker-compose -f docker/compose/docker-compose-dev.yml down
	$(CLI) run --rm --no-deps php_cli php -d memory_limit=-1 /usr/local/bin/composer update
	docker-compose -f docker/compose/docker-compose-dev.yml up -d

.PHONY: install
install:
	$(CLI) run --rm --no-deps php_cli php -d memory_limit=-1 /usr/local/bin/composer install

.PHONY: update
update:
	$(CLI) run --rm --no-deps php_cli php -d memory_limit=-1 /usr/local/bin/composer update

.PHONY: test32
test32:
	code/vendor/bin/phpcs -w -p -s --standard=code/vendor/flyeralarm/php-code-validator/ruleset.xml code/src/

.PHONY: test
test:
	php -dxdebug.coverage_enable=1 -dxdebug.mode=coverage code/vendor/bin/phpunit --coverage-clover code/tests/reports/phpunit.coverage.xml --coverage-html code/tests/reports/ --configuration code/tests/phpunit.xml code/tests/unit/
	
.PHONY: autoloader
autoloader:	$(CLI) run --rm --no-deps php_cli php -d memory_limit=-1 /usr/local/bin/composer dump-autoload
