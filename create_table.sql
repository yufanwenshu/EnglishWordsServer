CREATE TABLE `user` (
    `id` int (11) NOT NULL AUTO_INCREMENT,
    `username` varchar (100) NULL DEFAULT '',
    `password` varchar (100) NULL DEFAULT '',
    `name` varchar (100) NULL DEFAULT '',
    `nickname` varchar (100) NULL DEFAULT '',
    `sex` enum ('女', '其他', '男') NULL DEFAULT '其他',
    `telephone` varchar (100) NULL DEFAULT '',
    `email` varchar (100) NULL DEFAULT '',
    `register_date` date NULL,
    `birthday` date NULL,
    `issuper` boolean NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`)
) COMMENT = "存储用户信息" ENGINE = innodb DEFAULT CHARACTER SET = "utf8" COLLATE = "utf8_general_ci"

INSERT INTO
    `user` (
        `username`,
        `password`,
        `name`,
        `nickname`,
        `sex`,
        `telephone`,
        `email`,
        `register_date`,
        `birthday`,
        `issuper`
    )
VALUES
    (
        'yufanwenshu',
        'cwj010728',
        '赵梵宇',
        '宇梵文书',
        '男',
        '15225931333',
        '1365240381@qq.com',
        '2023-03-31',
        '2001-04-20',
        1
    );