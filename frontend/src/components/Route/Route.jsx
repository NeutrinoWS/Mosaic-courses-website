import cls from './Route.module.scss';
import indicator from '../../images/indicator.svg';

export const Route = () => {
  return (
    <div className={cls.route}>
      <ul className={cls.routeItems}>
        <li>
          <a href="!#" className={cls.routeItem}>
            Главная
          </a>
        </li>
        <li>
          <a href="!#" className={cls.routeItem}>
            <img
              className={cls.indicator}
              src={indicator}
              alt="Промо картинка"
            />
          </a>
        </li>
        <li>
          <a href="!#" className={cls.routeItem}>
            {' '}
            Курсы
          </a>
        </li>
        <li>
          <a href="!#" className={cls.routeItem}>
            <img
              className={cls.indicator}
              src={indicator}
              alt="Промо картинка"
            />
          </a>
        </li>
        <li>
          <a href="!#" className={cls.routeItemGreen}>
            {' '}
            Курс по Римской мозайке
          </a>
        </li>
      </ul>
    </div>
  );
};
